#include <fstream>
#include <iostream>
#include <memory>
#include <vector>
#include <unordered_map>
#include "schedule_unit.h"
#include "schedule.h"

using namespace std;



// Parse input files
unordered_map<int, vector<ScheduleUnit>>
  parse_configurations_file(string configurations_file)
{
  std::ifstream infile(configurations_file);
  int app_id, num_frozen, fps;
  double cost, metric;
  unordered_map<int, vector<ScheduleUnit>> possible_configurations = {};
  while (infile >> app_id >> num_frozen >> fps >> cost >> metric)
  {
    vector<ScheduleUnit> units; 
    ScheduleUnit unit = ScheduleUnit(app_id, num_frozen, fps, cost, metric);

    if (possible_configurations.find(app_id) == possible_configurations.end()) {
      units = {};
    } else {
      units = possible_configurations[app_id];
    }
    units.push_back(unit);
    possible_configurations.insert(make_pair(app_id, units));
    possible_configurations[app_id] = units;
  }
  return possible_configurations;
}

vector<double> parse_model_file(string model_file)
{
  vector<double> layer_costs = {};

  std::ifstream infile(model_file);
  std::string delimiter = ",";
  if (infile.good())
  {
    string line;
    getline(infile, line);

    size_t pos = 0;
    double token;
    std::string token_str;
    std::string::size_type sz;

    while ((pos = line.find(delimiter)) != std::string::npos) {
          token_str = line.substr(0, pos);
          token = stod(token_str, &sz);
          layer_costs.push_back(token);
          line.erase(0, pos + delimiter.length());
    }
  }
  return layer_costs;
}

unordered_map<int, int> get_next_configuration(unordered_map<int, int> config,
                                               unordered_map<int, vector<ScheduleUnit>> possible_configs,
                                               vector<int> app_ids){
  // Note: Vector of app_ids is used to maintain ordering

  // Initialization case
  if (config.size() == 0){
    for (auto const & app_id : app_ids) {
      config.insert(make_pair(app_id, 0));
    }
    return config;
  }

  // "Increment" config
  for (auto const & app_id : app_ids) {
    int num_options = possible_configs[app_id].size();
    int next_index = config[app_id] + 1;
    if (next_index + 1  <= num_options) {
      config[app_id] = next_index;
      return config;
    }
    config[app_id] = 0;
  }

  // If we haven't returned config yet, the last index "overflowed"
  // and there are no more configurations

  return {};
}

// For a given schedule-configuration, get the optimal schedule
// TODO: Prune possible configurations
unique_ptr<Schedule> get_optimal_schedule(string configurations_file,
                                          string model_file)
{
  unordered_map<int, vector<ScheduleUnit>> possible_configurations = 
    parse_configurations_file(configurations_file);
  vector<double> layer_costs = parse_model_file(model_file);

  std::vector<int> keys;
  keys.reserve(possible_configurations.size());
  for (auto kv: possible_configurations) {
    keys.push_back(kv.first);
  }

  unique_ptr<Schedule> best_schedule = make_unique<Schedule>(layer_costs);

  unordered_map<int, int> config = {};
  config = get_next_configuration(config, possible_configurations, keys);

  while (config.size() > 0){


    unique_ptr<Schedule> schedule = make_unique<Schedule>(layer_costs);

    for (auto const& c : config) {
      int app_id = c.first;
      int config_index = c.second;
      cout << config_index << " ";
      ScheduleUnit unit = possible_configurations[app_id][config_index];
      schedule->AddApp(unit);
    }
    cout << "\n";

    config = get_next_configuration(config, possible_configurations, keys);
  }

  return best_schedule;
}

int main()
{
  string configurations_file = "data/cpp/configurations/test.v0";
  string model_file = "data/cpp/models/test.v0";
  get_optimal_schedule(configurations_file,
                       model_file);

  cout << "Hello world!\n";
}

DATA_DIR="data/cpp/"
DATASETS="cars cats flowers pedestrian"
RUN_ID="test.v0"
VERBOSE=0
NUM_APPS_RANGE=3
NUM_SETUPS=15
STREAM_FPS=10
SETUP_CONFIG="config/scheduler/setup.v0"
SETUPS_FILE=$DATA_DIR"/setups."$RUN_ID

# Only need to generate this once
python src/scheduler/generate_setups.py -r $RUN_ID \
                                        -n $NUM_APPS_RANGE \
                                        -o $DATA_DIR \
                                        -s $NUM_SETUPS \
                                        -f $STREAM_FPS \
                                        -c $SETUP_CONFIG

python src/scheduler/exhaustive_search.py -v $VERBOSE \
                                          -o $DATA_DIR \
                                          -r $RUN_ID \
                                          -s $SETUPS_FILE \
                                          -n $NUM_APPS_RANGE

g++ -std=c++0x  src/scheduler/cpp/exhaustive_search.cpp \
                src/scheduler/cpp/schedule.cpp \
                src/scheduler/cpp/schedule_unit.cpp \
                && ./a.out

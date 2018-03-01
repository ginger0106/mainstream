#!/bin/bash
sem -j+0 python src/scheduler/run_scheduler_simulator.py 40 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-cars-cats-pedestrian-train-500 -m f1 --datasets cars cats pedestrian train > log/distributed/inception-f1-cars-cats-pedestrian-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 40 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-cars-cats-pedestrian-flowers-500 -m f1 --datasets cars cats pedestrian flowers > log/distributed/inception-f1-cars-cats-pedestrian-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 40 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-cars-cats-train-flowers-500 -m f1 --datasets cars cats train flowers > log/distributed/inception-f1-cars-cats-train-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 40 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-cars-pedestrian-train-flowers-500 -m f1 --datasets cars pedestrian train flowers > log/distributed/inception-f1-cars-pedestrian-train-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 40 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-cats-pedestrian-train-flowers-500 -m f1 --datasets cats pedestrian train flowers > log/distributed/inception-f1-cats-pedestrian-train-flowers-500-mainstream-simulator.out
sem --wait
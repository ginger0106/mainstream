#!/bin/bash
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-cats-pedestrian-500 -m f1 --scheduler hifi --budget 300 --datasets cars cats pedestrian > log/distributed/inception-f1-hifi-cars-cats-pedestrian-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-cats-train-500 -m f1 --scheduler hifi --budget 300 --datasets cars cats train > log/distributed/inception-f1-hifi-cars-cats-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-cats-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cars cats flowers > log/distributed/inception-f1-hifi-cars-cats-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-pedestrian-train-500 -m f1 --scheduler hifi --budget 300 --datasets cars pedestrian train > log/distributed/inception-f1-hifi-cars-pedestrian-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-pedestrian-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cars pedestrian flowers > log/distributed/inception-f1-hifi-cars-pedestrian-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-train-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cars train flowers > log/distributed/inception-f1-hifi-cars-train-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-pedestrian-train-500 -m f1 --scheduler hifi --budget 300 --datasets cats pedestrian train > log/distributed/inception-f1-hifi-cats-pedestrian-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-pedestrian-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cats pedestrian flowers > log/distributed/inception-f1-hifi-cats-pedestrian-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-train-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cats train flowers > log/distributed/inception-f1-hifi-cats-train-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 30 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-pedestrian-train-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets pedestrian train flowers > log/distributed/inception-f1-hifi-pedestrian-train-flowers-500-mainstream-simulator.out
sem --wait

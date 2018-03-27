#!/bin/bash
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-cats-500 -m f1 --scheduler hifi --budget 300 --datasets cars cats > log/distributed/inception-f1-hifi-cars-cats-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-pedestrian-500 -m f1 --scheduler hifi --budget 300 --datasets cars pedestrian > log/distributed/inception-f1-hifi-cars-pedestrian-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-train-500 -m f1 --scheduler hifi --budget 300 --datasets cars train > log/distributed/inception-f1-hifi-cars-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cars-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cars flowers > log/distributed/inception-f1-hifi-cars-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-pedestrian-500 -m f1 --scheduler hifi --budget 300 --datasets cats pedestrian > log/distributed/inception-f1-hifi-cats-pedestrian-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-train-500 -m f1 --scheduler hifi --budget 300 --datasets cats train > log/distributed/inception-f1-hifi-cats-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-cats-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets cats flowers > log/distributed/inception-f1-hifi-cats-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-pedestrian-train-500 -m f1 --scheduler hifi --budget 300 --datasets pedestrian train > log/distributed/inception-f1-hifi-pedestrian-train-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-pedestrian-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets pedestrian flowers > log/distributed/inception-f1-hifi-pedestrian-flowers-500-mainstream-simulator.out
sem -j+0 python src/scheduler/run_scheduler_simulator.py 20 ../mainstream-analysis/output/streamer/scheduler/distributed/f1/inception/f1-hifi-train-flowers-500 -m f1 --scheduler hifi --budget 300 --datasets train flowers > log/distributed/inception-f1-hifi-train-flowers-500-mainstream-simulator.out
sem --wait
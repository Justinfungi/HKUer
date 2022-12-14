#! /bin/bash


ssh -X fung0311@gpu2gate1.cs.hku.hk

gpu-interactive
hostname -I  
jupyter-lab --no-browser
10.64.32.123 
ssh -L 8888:localhost:8888 fung0311@10.64.32.123 

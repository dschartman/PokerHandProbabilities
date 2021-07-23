#!/bin/bash

. ${CONDA_SCRIPT}

conda create -n poker_kata -y python pytest black pylint rope pytest-watch isort
conda activate poker_kata
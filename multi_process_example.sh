# !/bin/bash

for i in {0..99}; do
{
    python3 processor_example.py --rank $i &
}
done
wait

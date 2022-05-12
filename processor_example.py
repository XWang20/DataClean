import json
from tqdm import tqdm
from clean_data import SingleProcess
import argparse
import time
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=str, help="name of dataset in the namespace")
    return parser.parse_args()

def main(args):
    start_time = time.time()
    input_path = f"/data/private/wangxing/OpenSoCo/original/"
    output_path = f"/data/private/wangxing/OpenSoCo/processed/"

    print(f"======= Start Processing {args.rank} =======")
    for i in tqdm(range(45)):
        f_in = open(os.path.join(input_path, f"en/{args.rank}_{i}.json"), "r")
        f_out = open(os.path.join(output_path, f"original/{args.rank}_{i}.json"), "w")
        f_repost_out = open(os.path.join(output_path, f"repost/{args.rank}_{i}.json"), "w")

        # f_in_lines = file_len(f_in)

        # 处理数据
        for line in f_in:
            message = SingleProcess(json.loads(line.strip()))
            if message:
                if "repost" in message.keys():
                    f_repost_out.write(json.dumps(message, ensure_ascii=False) + "\n")
                else:
                    f_out.write(json.dumps(message, ensure_ascii=False) + "\n")

        f_in.close()
        f_out.close()
        f_repost_out.close()

    print(f"======= Finish Processing {args.rank} =======")
    print("Time: ", time.time()-start_time)

if __name__ == '__main__':
    args = get_args()
    main(args)

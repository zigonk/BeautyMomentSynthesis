print("-----Initializing-----")

import argparse
import time
from SDD_FIQA import *
from animations.animations import *
from face_reg.detection import *
from SmileScore.smileScore import *
from animations.make_video import *
import datetime
from misc.log import *
from config import *
from misc.visualize import *

import warnings
warnings.filterwarnings('ignore')


def parse_args():
    parser = argparse.ArgumentParser(description='Face Detection and Recognition',
                                     usage='A module to detect and recognize faces in pictures')

    parser.add_argument('--anchor_dataset_path',
                        help='Path to your folder containing anchor images',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('--original_dataset_path',
                        help='Path to your folder containing input images',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('--output_path',
                        help='Output video path',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('--number_of_images',
                        help='Number of images will be presented in the video',
                        type=int,
                        required=False,
                        default=6)

    parser.add_argument('--effect_speed',
                        help='Video args',
                        type=int,
                        required=False,
                        default=1)

    parser.add_argument('--duration',
                        help='Video args',
                        type=int,
                        required=False,
                        default=3)

    parser.add_argument('--fps',
                        help='Video args',
                        type=int,
                        required=False,
                        default=75)
                        
    parser.add_argument('--fraction',
                        help='Resize images',
                        type=float,
                        required=False,
                        default=1)

    parser.add_argument('--find_person',
                        help='Find the person',
                        type = str,
                        required=False,
                        default=None)
                        
    parser.add_argument('--log',
                        help='Find the person',
                        type=bool,
                        required=False,
                        default=False)

    parser.add_argument('--visualize_boxes',
                        help='Visualizing bounding boxes in the video',
                        type=bool,
                        required=False,
                        default=False)

    args = parser.parse_args()
    return args


def main():
  args = parse_args()
  finding_names = args.find_person.split()
  print('People we need to identify:', finding_names)
  print('Used device: ', config.DEVICE)

  input_paths, input_names = return_paths(args.original_dataset_path, 'input')
  anchor_paths, anchor_labels = return_paths(args.anchor_dataset_path, 'anchor')

  append_df = []
  for batch_index in range(len(input_paths)):
    df, input_img = face_detection(input_paths[batch_index], input_names[batch_index], anchor_paths, anchor_labels, finding_names)
    df, input_img = FIQA(df, input_img)
    smile_model = load_smile_model(CFG_SMILE.MODEL_PATH)
    df, input_img = get_smile_score(df, input_img, smile_model)
    append_df.append(df)

    print('Finished batch {}'.format(batch_index + 1))

  df_final = pd.concat(append_df)
  df_final.sort_values(by = 'smile score average', ascending = False, inplace = True)
  df_final.reset_index(drop = True)

  df_final = df_final.iloc[:args.number_of_images]
  input_img = read_images(list(df_final['paths']), purpose = 'input')

  if args.visualize_boxes:
    input_img = visualizing_bounding_boxes(df_final, input_img)

  make_video(img_list = input_img,
             output_path = args.output_path,
             effect_speed = args.effect_speed,
             duration = args.duration,
             fps = args.fps,
             fraction = args.fraction)


if __name__ == '__main__':
    main()

import os
import sys
import time


def play_video(path):

    cv2.destroyAllWindows()
    video = cv2.VideoCapture(path)
    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
    fps = float(video.get(cv2.CAP_PROP_FPS))
    print('\nPress spacebar to advance 1 frame, press "q" to exit!')
    print(f"fps: {round(fps,3)}\n")
    i = 1
    while video.isOpened():
        if i == length + 1:
            video.release()
            cv2.destroyAllWindows()
            break
        print(f"Frame: {i}/{length}, time: {round(i/fps,4)} s")
        i += 1

        ret, frame = video.read()
        time.sleep(0.01)
        cv2.imshow("video", frame)
        key = cv2.waitKey(0)
        while key not in [ord("q"), ord(" ")]:
            key = cv2.waitKey(0)
        if key == ord("q") and video.isOpened():
            break
    print("Done\n", end="")


if __name__ == "__main__":

    try:
        import cv2

        print(
            "=====================================\nMade by Bror Hjemgaard for CCSE, 2020\n====================================="
        )

        print("Please enter the local path of the video file")
        path = input(">> ")
        assert os.path.exists(path)

        if sys.platform == "linux":
            print(
                "linux platform detected. Please note that the OpenCV library is unstable with some distros, and you may need to run the script on windows in some cases. Sometimes the problem is fixed by just pressing spacebar enough times"
            )
        play_video(path)
    except IndexError:
        print("No file name given. Please include file name as argument")
    except AssertionError:
        print(f"No file named '{path}' found")
    except ModuleNotFoundError:
        print(
            'You do not have the module "OpenCV" installed. Install it with "pip install opencv-python". '
        )
    sys.exit()

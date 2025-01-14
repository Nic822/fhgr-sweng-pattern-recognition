__author__ = "KLSA"
__copyright__ = "Copyright 2023 to Infinity and Beyond, CEDES AG"

import cv2
from image_proc.image_proc import ImageProcessor
from pattern_logger.console_logger import ConsolePatternLogger
from pattern_logger.csv_logger import CsvPatternLogger
from visualizer.visualizer import Visualizer


class App:
    def __init__(self):
        self.image_processor = ImageProcessor()
        self.visualizer = Visualizer("MyVis")
        self.loggers = [
            ConsolePatternLogger(),
            CsvPatternLogger(),
        ]

    def run(self):
        try:
            while True:
                frame = cv2.imread("assets/test_image.JPG", cv2.IMREAD_COLOR)
                pattern_list = self.image_processor.process(frame)

                for logger in self.loggers:
                    logger.log(pattern_list)

                self.visualizer.visualize(frame, pattern_list)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        except KeyboardInterrupt:
            pass
        finally:
            cv2.destroyAllWindows()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()

# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import logging
import sys

from PIL import Image


LOGGING_FORMATTER = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")


def get_console_handler(logging_formatter=LOGGING_FORMATTER):
    """
    Return a logging handler that sends logging output to the system's
    standard output.


    :param logging_formatter: An object `Formatter` to set for this handler.


    :return: An instance of the `StreamHandler` class.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging_formatter)
    return console_handler


def main():
    arguments = parse_arguments()
    setup_logger(logging_level=logging.DEBUG)


def parse_arguments():
    """
    Convert argument strings to objects and assign them as attributes of
    the namespace.


    @return: an instance `Namespace` corresponding to the populated
        namespace.
    """
    parser = argparse.ArgumentParser(description='QR Code Decoder')

    parser.add_argument(
        '-f', '--file',
        dest='file_path_name',
        metavar='FILE',
        required=True,
        help="specify the absolute path and name of the image file to produce a biometric passport photo")

    return parser.parse_args()


def setup_logger(
        logging_formatter=LOGGING_FORMATTER,
        logging_level=logging.INFO,
        logger_name=None):
    """
    Setup a logging handler that sends logging output to the system's
    standard output.


    :param logging_formatter: An object `Formatter` to set for this handler.

    :param logger_name: Name of the logger to add the logging handler to.
        If `logger_name` is `None`, the function attaches the logging
        handler to the root logger of the hierarchy.

    :param logging_level: The threshold for the logger to `level`.  Logging
        messages which are less severe than `level` will be ignored;
        logging messages which have severity level or higher will be
        emitted by whichever handler or handlers service this logger,
        unless a handler’s level has been set to a higher severity level
        than `level`.


    :return: An object `Logger`.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)
    logger.addHandler(get_console_handler(logging_formatter=logging_formatter))
    logger.propagate = False
    return logger


if __name__ == '__main__':
    main()

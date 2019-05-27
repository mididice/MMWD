import os
import sys

from magenta import music as mm
from magenta.models.music_vae import configs
from magenta.models.music_vae import TrainedModel
import numpy as np
import tensorflow as tf
import itertools

flags = tf.app.flags
logging = tf.logging
FLAGS = flags.FLAGS

config = configs.CONFIG_MAP['cat-mel_2bar_big']


def _check_extract_examples(input_ns, path, input_number):
    """Make sure each input returns exactly one example from the converter."""
    tensors = config.data_converter.to_tensors(input_ns).outputs
    if not tensors:
        print(
        'MusicVAE configs have very specific input requirements. Could not '
        'extract any valid inputs from `%s`. Try another MIDI file.' % path)
        sys.exit()
    elif len(tensors) > 1:
        basename = os.path.join(
        '%s_input%d-extractions_%s-*-of-%03d.mid' %
        ("music-vae", input_number, 00, len(tensors)))
    for i, ns in enumerate(config.data_converter.to_notesequences(tensors)):
        mm.sequence_proto_to_midi_file(ns, basename.replace('*', '%03d' % i))
        print(
        '%d valid inputs extracted from `%s`. Outputting these potential '
        'inputs as `%s`. Call script again with one of these instead.' %
        (len(tensors), path, basename))
        sys.exit()
    logging.info('Attempting to extract examples from input MIDIs using config `%s`...', FLAGS.config)


def make_music_vae(input_midi_file_1, input_midi_file_2):
    input_midi_1 = os.path.expanduser(input_midi_file_1)
    input_midi_2 = os.path.expanduser(input_midi_file_2)
    if not os.path.exists(input_midi_1):
        raise ValueError('Input MIDI 1 not found: %s' % input_midi_file_1)

    if not os.path.exists(input_midi_2):
        raise ValueError('Input MIDI 2 not found: %s' % input_midi_file_2)
    input_1 = mm.midi_file_to_note_sequence(input_midi_1)
    input_2 = mm.midi_file_to_note_sequence(input_midi_2)

    _check_extract_examples(input_1, input_midi_file_1, 1)
    _check_extract_examples(input_2, input_midi_file_2, 2)


midi_list = ['A.mid','B.mid','C.mid','D.mid','E.mid','F.mid','G.mid','H.mid','I.mid','J.mid','K.mid','L.mid','M.mid','N.mid','O.mid','P.mid']
event = list(itertools.permutations(midi_list, 2))
for i in event:
    make_music_vae(i[0], i[1])

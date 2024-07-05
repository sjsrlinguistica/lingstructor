import os

def get_phonemes_path():
    # Get the absolute path to the directory containing this script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to phonemes.json relative to this script's directory
    return os.path.join(base_path, 'cache', 'phonemes.json')

def get_syllable_parameters_path():
    # Get the absolute path to the directory containing this script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to syllable_parameters.json relative to this script's directory
    return os.path.join(base_path, 'cache', 'syllable_parameters.json')

def get_syllable_structure_path():
    # Get the absolute path to the directory containing this script
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to syllable_structure.json relative to this script's directory
    return os.path.join(base_path, 'cache', 'syllable_structure.json')


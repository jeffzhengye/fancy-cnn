"""
prepare-yelp.py

description: prepare the Yelp data for training in DNNs
"""
import cPickle as pickle
import logging

import numpy as np

from nlpdatahandlers import YelpDataHandler
from wordvectors.glove import GloVeBox

LOGGER_PREFIX = ' %s'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def log(msg, logger=logger):
    logger.info(LOGGER_PREFIX % msg)

YELP_USEFUL_TRAIN = '../yelp-dataset/TrainSet_useful_185292'
YELP_USEFUL_DEV = '../yelp-dataset/DevSet_useful_185292'
YELP_USEFUL_TEST = '../yelp-dataset/TestSet_useful_185292'

YELP_FUNNY_TRAIN = '../yelp-dataset/TrainSet_funny_75064'
YELP_FUNNY_DEV = '../yelp-dataset/DevSet_funny_75064'
YELP_FUNNY_TEST = '../yelp-dataset/TestSet_funny_75064'

YELP_COOL_TRAIN = '../yelp-dataset/TrainSet_cool_88698'
YELP_COOL_DEV = '../yelp-dataset/DevSet_cool_88698'
YELP_COOL_TEST = '../yelp-dataset/TestSet_cool_88698'

GLOBAL_WV_FILE = './data/wv/glove.42B.300d.120000.txt'
WORDS_PER_TEXT = 300

if __name__ == '__main__':

    log('Building global word vectors from {}'.format(GLOBAL_WV_FILE))
    global_gb = GloVeBox(GLOBAL_WV_FILE)
    global_gb.build(zero_token=True, normalize_variance=False, normalize_norm=True)

    log('writing GloVeBox pickle...')
    pickle.dump(global_gb, open(GLOBAL_WV_FILE.replace('.txt', '-glovebox.pkl'), 'wb'), pickle.HIGHEST_PROTOCOL)

    yelp = YelpDataHandler()

    log('Loading "useful" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_USEFUL_TRAIN, YELP_USEFUL_DEV, YELP_USEFUL_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_useful_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_useful_train_fulltext_glove_300_y.npy', train_labels)

    del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_useful_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_useful_test_fulltext_glove_300_y.npy', test_labels)

    del reviews_wvs_test

    log('Loading "funny" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_FUNNY_TRAIN, YELP_FUNNY_DEV, YELP_FUNNY_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_funny_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_funny_train_fulltext_glove_300_y.npy', train_labels)

    del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_funny_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_funny_test_fulltext_glove_300_y.npy', test_labels)

    del reviews_wvs_test

    log('Loading "cool" votes data')
    (train_reviews, train_labels, test_reviews, test_labels) = \
        yelp.get_data(YELP_COOL_TRAIN, YELP_COOL_DEV, YELP_COOL_TEST)

    reviews_wvs_train = yelp.to_word_level_idx(train_reviews, global_gb, WORDS_PER_TEXT)
    # -- training data save
    np.save('Yelp_cool_train_fulltext_glove_300_X.npy', reviews_wvs_train)
    np.save('Yelp_cool_train_fulltext_glove_300_y.npy', train_labels)

    del reviews_wvs_train

    reviews_wvs_test = yelp.to_word_level_idx(test_reviews, global_gb, WORDS_PER_TEXT)
    # -- testing data save
    np.save('Yelp_cool_test_fulltext_glove_300_X.npy', reviews_wvs_test)
    np.save('Yelp_cool_test_fulltext_glove_300_y.npy', test_labels)

    del reviews_wvs_test
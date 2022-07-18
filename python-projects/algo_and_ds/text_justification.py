from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        word_lengths = [len(w) for w in words]
        start = 0
        end = 0
        while end < len(words):
            buffer = maxWidth
            end_ = end
            while buffer > 0:
                buffer -= word_lengths[end_]
                buffer -= 1 # for a space
                end_ += 1
            if buffer == 0:
                end_ -= 1


def find_end(words, word_lengths, maxWidth, start):
    buffer = maxWidth
    end_ = start
    word_coverage = 0
    while buffer > 0:
        buffer -= word_lengths[end_]
        if buffer >= 0:
            word_coverage += word_lengths[end_]
            buffer -= 1 # for a space
            end_ += 1
        print(f'{buffer=}, {end_=}')
    if buffer < 0:
        word_coverage -= word_lengths[end_]
        end_ -= 1
    end = end_
    print(f'{words[start:end+1]=}')
    return end, word_coverage


def get_space_distribution(space_coverage, start, end):
    spaces = []
    nbreaks = end - start # should be one less as number of breaks are less than the number of words
    while space_coverage > 0 and nbreaks > 0:
        curr_spaces = (space_coverage // nbreaks) + (space_coverage % nbreaks)
        spaces.append(' ' * curr_spaces)
        space_coverage -= curr_spaces
        nbreaks -= 1
    return spaces

def create_line(words, space_distribution, start, end):
    line = []
    for i in range(start, end+1):
        line.append(words[i])
        if i < end:
            line.append(space_distribution[i-start])
    return "".join(line)


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    output = []
    word_lengths = [len(w) for w in words]
    start = 0
    while start < len(words):
        end, word_coverage = find_end(words, word_lengths, maxWidth, start)
        space_coverage = maxWidth - word_coverage
        print(end, word_coverage, space_coverage)
        space_distribution = get_space_distribution(space_coverage, start, end)
        print(f'{space_distribution=}')
        line = create_line(words, space_distribution, start, end)
        print(f'{line=}')
        output.append(line)
        start = end + 1
    return output
        

from pprint import pprint

# words = ['this']
# maxWidth = 4
# pprint(fullJustify(words, maxWidth))

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
pprint(fullJustify(words, maxWidth))
import sys
import string
import random

def process_file(filename):
	linegram = []
	fp = open(filename)
	for line in fp:
		process_line(line, linegram)
	return linegram

def process_line(line, linegram):
	line = line.replace('-', ' ')

	for word in line.split():
		#word = word.strip(string.punctuation + string.whitespace + '.')
		word = word.lower()

		linegram.append(word)

def markov(linegram, prefix_count):
	result = dict()
	for index, value in enumerate(linegram[:-(prefix_count)]):
		# Build prefixes
		this_prefix = (value,)
		for i in range(1, prefix_count):
			this_prefix = this_prefix + (linegram[index + i],)
		#print this_prefix
		sufix = linegram[index + prefix_count]

		# Attach new sufix
		if this_prefix in result:
			result[this_prefix].append(sufix)
		else:
			result[this_prefix] = [sufix]
	return result

def shift(prefix, word):
	return prefix[1:] + (word,)

def ran_mark(dictionary, total):
	keys = dictionary.keys()
	aleatoreidad = 0
	
	last = keys[random.randint(0, len(dictionary) - 1)] # Gets a prefix
	result = list(last)
	#print "first is", last

	for i in range(total):
		if last not in dictionary:
			break
		sufixes = dictionary[last]
		#print "sufixes for", last, "are", sufixes
		if len(sufixes) > 0:
			if len(sufixes) != 1:
				aleatoreidad += 1
			new_sufix = sufixes[random.randint(0, len(sufixes) - 1)]
			result.append(new_sufix)
			last = shift(last, new_sufix)
			#print "last is", last
		else:
			break
	print "aleatoreidad =", (aleatoreidad / total)
	return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        markov_level = int(sys.argv[2])
        count = int(sys.argv[3])
        linegram = process_file(filename)
        m = markov(linegram, markov_level)
        print ran_mark(m, count)
        #print m

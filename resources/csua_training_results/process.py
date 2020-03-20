#!/usr/bin/env python3
"""
Generate plots for loss etc.
"""
import click
import numpy as np
import matplotlib.pyplot as plt
import re
import types

def fileop(filename, op):
    with open(filename) as f:
        return op(f)

def read(name):
    return fileop(name, lambda f: f.read())

def readlines(name, trim=False):
    readline_op = lambda f: f.readlines()
    if trim:
        op = lambda f: [line.trim() for line in readline_op(f)]
    else:
        op = readline_op
    return fileop(name, lambda f: f.readlines()) 

def get_losses(log_name):
    lines = readlines(log_name, trim=True)
    pattern = '^INFO(?:.*?)Epoch (\d*) Rank (\d*).*Train loss: \((.*?)\), Test loss \((.*?)\)$'
    pattern = re.compile(pattern)
    results = [pattern.search(line) for line in lines]
    results = [parse_match(result) for result in results if result is not None]
    return invert(results)

def parse_nums(nums):
    return [float(num.strip(',')) for num in nums.split()]

def parse_match(match):
    epoch, rank, train_loss, test_loss = match.groups()
    epoch = int(epoch)
    rank = int(rank)
    train_loss = parse_nums(train_loss)
    test_loss = parse_nums(test_loss)
    return {'epoch': epoch,
            'rank': rank,
            'train_loss': train_loss,
            'test_loss': test_loss}

def invert(losses):
    if not losses:
        return {}
    keys = losses[0].keys()
    losses = {key: [loss[key] for loss in losses] for key in keys}
    losses['train_loss'] = invert_train_loss(losses['train_loss'])
    losses['test_loss'] = invert_train_loss(losses['test_loss'])
    return losses

def invert_train_loss(losses):
    return [[loss[i] for loss in losses] for i in range(len(losses[0]))]

def flatten(l):
    return [element for sublist in l for element in sublist]

def clip(l, a, b):
    return [max(min(b, e), a) for e in l]
 
@click.group()
def main():
    pass

@main.command()
@click.argument('log')
@click.option('--key', default='train_loss')
def hist(log, key):
    losses = flatten(get_losses(log)[key])
    fig = plt.figure()
    fig.suptitle(f'{key} histograms')
    ax = [fig.add_subplot(221), fig.add_subplot(222),
          fig.add_subplot(223), fig.add_subplot(224)]
    ax[0].hist(losses, bins=200)
    ax[0].set_title('No clipping')
    ax[1].hist(clip(losses, 0, 10), bins=200)
    ax[1].set_title('Clip to 10')
    ax[2].hist(clip(losses, 0, 6), bins=200)
    ax[2].set_title('Clip to 6')
    ax[3].hist(clip(losses, 0, 5), bins=200)
    ax[3].set_title('Clip to 5')
    for axis in ax:
        axis.set_xlabel('loss')
        axis.set_ylabel('# epochs')
    fig.tight_layout(pad=2)
    plt.savefig(f'{key}_hist.png')

@main.command()
@click.argument('log')
def analyze(log):
    losses = get_losses(log)
    for i, (train_loss, test_loss) in enumerate(zip(losses['train_loss'], losses['test_loss'])):
        plt.clf()
        train_loss = [min(6, l) for l in train_loss]
        plt.plot(range(len(losses['epoch'])), train_loss, label='train_loss')
        plt.plot(range(len(losses['epoch'])), test_loss, label='test_loss')
        plt.vlines(losses['epoch'][1:].index(0) + 1, 0, 6)
        plt.title(f"Loss for domain {i}")
        plt.xlabel("'epoch' (training was restarted around 400 on the graph, it's really epoch 0 again)")
        plt.ylabel("loss")
        plt.legend()
        plt.savefig(f'analysis_{i}.png')
    

if __name__ == '__main__':
    main()

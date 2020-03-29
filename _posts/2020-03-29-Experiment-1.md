---
layout: post
title: [ Inference with In and Out of Domain Samples]
---

# Inference with In and Out of Domain Samples

## Summary

The purpose of this experiment was to somewhat tangentially replicate the paper's experiment with in and out of domain samples with the pretrained model and .wav samples we collected on our own, so this would be easily comparable to our trained model and so we can more objectively test this on our own/compare results to those of the paper. We ran samples through the encoder and decoder to get outputs, then ran the outputs through the encoder again to compare with the encoder outputs from the original file.

## Samples
We collected 10 short (~10 sec) music samples on Youtube of various samples/domains not included in the training dataset for the pretrained model, including classical solo music on various instruments, Chinese classical music, jazz, and rock. In general, the model performed fairly well for classical music with more distinct tones, but poorly for music that was out of domain and/or included percussion or other non-instrumental sounds.


## Results (to piano)

[Original violin]({{site.url}}/resources/experiment_1/violin.wav)

[Violin to piano]({{site.url}}/resources/experiment_1/3_violin.wav)

[Original trumpet]({{site.url}}/resources/experiment_1/trumpet.wav)

[Trumpet to piano]({{site.url}}/resources/experiment_1/3_trumpet.wav)

[Original swing jazz]({{site.url}}/resources/experiment_1/swingjazz.wav)

[Swing jazz to piano]({{site.url}}/resources/experiment_1/3_swingjazz.wav)

[Original saxophone]({{site.url}}/resources/experiment_1/saxophone.wav)

[Saxophone to piano]({{site.url}}/resources/experiment_1/3_saxophone.wav)

[Original piano]({{site.url}}/resources/experiment_1/piano.wav)

[Piano to piano]({{site.url}}/resources/experiment_1/3_piano.wav)

[Original orchestra]({{site.url}}/resources/experiment_1/orchestra.wav)

[Violin to piano]({{site.url}}/resources/experiment_1/3_orchestra.wav)

[Original metal]({{site.url}}/resources/experiment_1/metalguitar.wav)

[Metal to piano]({{site.url}}/resources/experiment_1/3_metalguitar.wav)

[Original marimba]({{site.url}}/resources/experiment_1/marimba.wav)

[Marima to piano]({{site.url}}/resources/experiment_1/3_marimba.wav)

[Original Chinese]({{site.url}}/resources/experiment_1/chinese.wav)

[Chinese to piano]({{site.url}}/resources/experiment_1/3_chinese.wav)

[Original bassoon]({{site.url}}/resources/experiment_1/bassoon.wav)

[Bassoon to piano]({{site.url}}/resources/experiment_1/3_violin.wav)

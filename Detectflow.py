import json
import os, sys, subprocess, shlex, re
from subprocess import call

for line in open("audiolist").read().splitlines():
	cmnd = ['ffprobe', '-show_streams', '-print_format', 'json', '-loglevel', 'quiet', line]
	p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out = p.communicate()
	srt =  json.loads(out[0])
	rate = srt["streams"][0]["sample_rate"]
	ratenum = int(rate)
	if ratenum <> 44100:
		print line + ":sample_rate is low than 44100:" + ratenum

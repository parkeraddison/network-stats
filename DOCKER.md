# Running network-stats via Docker

The supplied Dockerfile can be used to create a container with all network-stats dependencies setup. This container can be used to run network-stats, and will monitor your local device network activity. This way you can avoid dealing with locally installing impacket and pcapy.

**Table of contents**
- [Prerequisities](#prerequisities)
- [Usage](#usage)
  - [Build the image](#build-the-image)
  - [Run the container](#run-the-container)
  - [Run network-stats](#run-network-stats)
  - [Save the results](#save-the-results)

## Prerequisities

In order to run this container the only requirement is docker itself.

See: https://docs.docker.com/get-docker/

## Usage

### Build the image
We can build an image from this Dockerfile, and name it something like 'network-stats'. To build the image, navigate to the root directory of this repository, then run
```bash
docker build -t network-stats .
```

### Run the container
By default, a docker container is given it's own IP address when run. However, we want the container to act as part of the same local machine we're browsing with. So, we must specify `--network host`. To run an instance of bash within the network-stats image, run
```bash
docker run -it --network host network-stats
```
Note that you can add the flag `--rm` in order to automatically delete the container once you exit.

### Run network-stats
From within the container, you can run network-stats as normal. (Note that the `$` is simply for documentation purposes to denote commands run from the container, versus locally)
```bash
$ python3 network-stats/list_interfaces.py
```
And start monitoring your connection to a csv using
```bash
$ python3 network-stats/network_stats.py -i INTERFACE -c FILENAME.csv
```

### Save the results
Finally, once you're done with monitoring (interrupt the container by pressing Ctrl+C twice) you can copy this file over to your local machine. First we must find the container name by locally running 
```bash
docker ps
```
Copy either the Name or Container ID to the clipboard, then duplicate the file from the container over to your current local directory by locally running
```bash
docker cp NAME_OR_ID:/home/FILENAME.csv .
```

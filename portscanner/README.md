# Port Scanner

## Overview

## Libraries

## Usage

## Examples

## Enhancements

- [ ] Concurrency: Use threading or asyncio to scan faster.
- [x] Banner Grabbing: After connecting, try receiving a few bytes (s.recv(1024)) to identify the service (e.g., HTTP, FTP).
- [ ] Customizable Input: Allow user to specify the host and port range from the command line.
- [ ] Error Handling: Handle cases where the hostname can’t be resolved.
- [ ] Output Formatting: Print results in a clean table.

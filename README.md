# nbprint example plugin

Example hydra plugin for nbprint

[![Build Status](https://github.com/nbprint/nbprint-example-plugin/actions/workflows/build.yml/badge.svg?branch=main&event=push)](https://github.com/nbprint/nbprint-example-plugin/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/nbprint/nbprint-example-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/nbprint/nbprint-example-plugin)
[![License](https://img.shields.io/github/license/nbprint/nbprint-example-plugin)](https://github.com/nbprint/nbprint-example-plugin)
[![PyPI](https://img.shields.io/pypi/v/nbprint-example-plugin.svg)](https://pypi.python.org/pypi/nbprint-example-plugin)

## Overview

This project demonstrates a [Hydra SearchPathPlugin](https://hydra.cc/docs/advanced/plugins/overview/), with a simple example configuration of a `page`.

> [!WARNING]
>
> Plugins should always namespace their configuration to not conflict with other plugins!
> E.g. here we put our page configuration in `page/<plugin name>/default.yaml`

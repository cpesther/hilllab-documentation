# hilllab.interfaces

Notebook interfaces that select paths and invoke the existing autotracker functions.

## Data and supporting resources

(resource-autotracker-ipynb)=

### autotracker.ipynb

Notebook interface for selecting video/save folders, running the batch tracker, and testing tracking parameters. It defines no new functions. Start with a small video and inspect the parameter test before a full batch.

These notebooks inherit the current autotracker import issue. Function contracts are in the [autotracker guide](../autotracker/index.md).

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/interfaces/autotracker.ipynb).

(resource-autotracker-parameter-test-ipynb)=

### autotracker_parameter_test.ipynb

Notebook interface for testing tracking parameters against a small set of frames. Replace the example path with your video location; it calls the existing parameter-test function rather than defining another API.

These notebooks inherit the current autotracker import issue. Function contracts are in the [autotracker guide](../autotracker/index.md).

[View resource source](https://github.com/cpesther/hilllab/blob/cc6789a0a8a3420c23f972ac041412275e7aa47a/hilllab/interfaces/autotracker_parameter_test.ipynb).

| [Home](/trick) → [Developer Docs](Developer-Docs-Home) → Testing |
|------------------------------------------------------------------|


# Testing

Currently, Trick has a suite of unit and integration tests that run through a hodgepodge of GTest, Trick's internal unit test framework, Makefiles, and TrickOps. 

Unit tests can be found in their respective `trick_source/[sim_services|utils]/*/test` directories, and primarily use the Gtest framework. These are run primarily through test targets in their Makefiles. See `trick_source/sim_services/MemoryManager/test` for an example of organization.

Integration tests take the form of Sims with some embedded tests. They live under `trick_sims/` and `test/`. A full list of sims that are used as part of the test suite are in [test_sims.yml](). These are run with TrickOps.

## Test suite dependencies

Gtest is required for the unit tests and some integration tests. See the [install guide](../documentation/install_guide/Install-Guide.md) for gtest installation.

TrickOps requires python3 and the packages `PyYAML` and `psutil` (updated list in [Trickops requirements.txt](https://github.com/nasa/trick/blob/master/share/trick/trickops/requirements.txt)). Install these in your python environment, or create a virtual environment as follows:
```
cd share/trick/trickops/
python3 -m venv .venv && . .venv/bin/activate && pip3 install -r requirements.txt
cd ../../../
```


## Running the test suite
From trick home:
```
# Run everything
make test

# Run only integration tests
make sim_test

# Run only unit tests
make unit_test
```

Currently, TrickOps will redirect all console output from tests into logs under {TRICK_HOME}/trickops_logs/, and will also dump the output of failing logs to console after the test suite is finished.

## Coverage
Trick uses [Coveralls](https://coveralls.io/github/nasa/trick?branch=master) to host code coverage. Coverage is generated by running the test suite with gcov in CI, and then those files are uploaded to Coveralls.

To enable gcov in Trick, it must be cleaned and compiled with the following:
```
export CFLAGS="-fprofile-arcs -ftest-coverage -O0"
export CXXFLAGS="-fprofile-arcs -ftest-coverage -O0"
export LDFLAGS="-fprofile-arcs -ftest-coverage -O0"
export TRICK_CFLAGS="-fprofile-arcs -ftest-coverage -O0"
export TRICK_CXXFLAGS="-fprofile-arcs -ftest-coverage -O0"
export TRICK_SYSTEM_LDFLAGS="-fprofile-arcs -ftest-coverage -O0"
export TRICK_SYSTEM_CFLAGS="-fprofile-arcs -ftest-coverage -O0"
export TRICK_SYSTEM_CXXFLAGS="-fprofile-arcs -ftest-coverage -O0"
```

After Trick has been rebuild with the instrumentation, run:
```
make code-coverage
```
This will generate, collect, and filter all the various coverage data collection files into `coverage.info`. This is the file that is uploaded to Coveralls in the [code_coverage.yml](https://github.com/nasa/trick/blob/master/.github/workflows/code_coverage.yml) Github Actions workflow.



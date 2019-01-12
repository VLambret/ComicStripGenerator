#!/usr/bin/env bats

CSG_COMMAND=../src/main.py

# Failure tests

@test "Given no parameters command fails" {
	run $COMMAND > /dev/null
	[ $status -ne 0 ]
	[ ! -f .png ]
}

@test "Given more than two parameters command fails" {
	run $COMMAND one too many> /dev/null
	[ $status -ne 0 ]
	[ ! -f one.png ]
}

@test "Given a non existing input file name command fails" {
	run $COMMAND dontexist.strip > /dev/null
	[ $status -ne 0 ]
	[ ! -f dontexist.png ]
}

@test "Given an empty input file command fails" {
	run $COMMAND empty.strip > /dev/null
	[ $status -ne 0 ]
	[ ! -f empty.png ]
}

@test "Given an invalid input file command fails" {
	run $COMMAND invalid.strip > /dev/null
	[ $status -ne 0 ]
	[ ! -f invalid.png ]
}

# Valid usage tests

@test "testing file existence" {
}

@test "Passing --help option print program usage on standard output" {
	run $COMMAND --help > /dev/null
	[ $status -eq 0 ]
	[ $output != "" ]
}

@test "Given a valid input file name command produce an output with default name" {
	run $COMMAND valid.strip > /dev/null
	[ $status -eq 0 ]
	[ $output = "" ]
	[ -f valid.png ]
}

@test "Given a valid input file name and a target name command produce an output with target name" {
	run $COMMAND valid.strip valid_alternate.png > /dev/null
	[ $status -eq 0 ]
	[ $output = "" ]
	[ -f valid_alternate.png ]
}

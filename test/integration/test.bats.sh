#!/usr/bin/env bats

CSG_COMMAND=../../src/main.py

# Failure tests

@test "Given no parameters command fails" {
	run $CSG_COMMAND
	[ $status -ne 0 ]
	[ ! -f .png ]
}

@test "Given more than two parameters command fails" {
	run $CSG_COMMAND one too many> /dev/null
	[ $status -ne 0 ]
	[ ! -f one.png ]
}

@test "Given a non existing input file name command fails" {
	run $CSG_COMMAND dontexist.strip > /dev/null
	[ $status -ne 0 ]
	[ ! -f dontexist.png ]
}

#@test "Given an empty input file command fails" {
#	run $CSG_COMMAND empty.strip > /dev/null
#	[ $status -ne 0 ]
#	[ ! -f empty.png ]
#}

@test "Given an invalid input file command fails" {
	run $CSG_COMMAND invalid.strip > /dev/null
	[ $status -ne 0 ]
	[ ! -f invalid.png ]
}

## Valid usage tests

@test "Passing --help option print program usage on standard output" {
	run $CSG_COMMAND --help > /dev/null
	[ $status -eq 0 ]
	[ $output != "" ]
}

@test "Given a valid input file name command produce an output with default name" {
	run $CSG_COMMAND valid.strip > /dev/null
	[ $status -eq 0 ]
	[ -f valid.strip.png ]
}

@test "Given a valid input file name and a target name command produce an output with target name" {
	run $CSG_COMMAND valid.strip valid_alternate.png > /dev/null
	[ $status -eq 0 ]
	[ -f valid_alternate.png ]
}

@test "test all valid files" {
	for VALID_FILE in valid*.strip
	do
		$CSG_COMMAND $VALID_FILE
		diff -q $VALID_FILE.png valid_references/$VALID_FILE.png
		echo $VALID_FILE
	done
}

@test "test staging files, not ready to be used as reference" {
	for STAGING_FILE in staging*.strip
	do
		$CSG_COMMAND $STAGING_FILE
		echo $STAGING_FILE
	done
}

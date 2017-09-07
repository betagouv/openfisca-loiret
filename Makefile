clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	openfisca-run-test openfisca_loiret/tests --country_package openfisca_france --extensions openfisca_loiret

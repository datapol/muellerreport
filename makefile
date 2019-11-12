# Mueller Report

# Clone other Mueller Report repos
clone:
	make _clone_mkdirs
	make _clone_repos

_clone_repos:
	@cd ../mueller_repos/gadenbuie; git clone https://github.com/gadenbuie/mueller-report.git
	@cd ../mueller_repos/iandennismiller; git clone https://github.com/iandennismiller/mueller-report.git
	@cd ../mueller_repos/batpigandme; git clone https://github.com/batpigandme/tidymueller.git
	@cd ../mueller_repos/rayrrr; git clone https://github.com/rayrrr/MuellerNLP.git
	@cd ../mueller_repos/pjaol; git clone https://github.com/pjaol/TheMuellerReport.git
	@cd ../mueller_repos/rayrrr; git clone https://github.com/rayrrr/MuellerNLP.git

_clone_mkdirs:
	@echo ""
	@echo "REPO: The Redacted Mueller Report - A text extraction"
	@mkdir --parents --verbose ../mueller_repos/gadenbuie/
	@# echo https://github.com/gadenbuie/mueller-report
	@echo ""
	@echo "REPO: Open Source Mueller Report (TeX)"
	@mkdir --parents --verbose ../mueller_repos/iandennismiller
	@# echo https://github.com/iandennismiller/mueller-report
	@echo ""
	@echo "REPO: Word frequencies in Mueller vs. Watergate Reports"
	@mkdir --parents --verbose ../mueller_repos/batpigandme
	@# echo https://github.com/batpigandme/tidymueller
	@echo ""
	@echo "REPO: Custom-length Mueller Report Summary documents with NLP (Natural Language Processing"
	@mkdir --parents --verbose ../mueller_repos/rayrrr
	@# echo https://github.com/rayrrr/MuellerNLP
	@echo ""
	@echo "REPO: Mueller Report NLP and Graphviz dot images"
	@mkdir --parents --verbose ../mueller_repos/pjaol
	@# echo https://github.com/pjaol/TheMuellerReport
	@echo ""
	@echo "REPO: Mueller Report Summarized with Python and NLP"
	@# echo https://github.com/rayrrr/MuellerNLP
	@echo ""
	@echo "REPO Dirs:"
	@find ../mueller_repos

pylint:
	@git status -uno | perl -ne 'if (/(\S+.py)/) {printf "echo $$1\npylint -r no %s\n", $$1}' | tee tmp_pylint
	chmod 755 tmp_pylint
	tmp_pylint

clean:
	rm -f tmp_pylint
	rm -f *.xlsx

clobber:
	rm -rf ../mueller_repos

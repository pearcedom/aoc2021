.PRECIOUS: src/day%/ans.txt
days := $(shell seq -f "%02g" $$(date -d "$D" '+%d'))

all: $(days)

%: src/day%/ans.txt
	@echo Day $*
	@cat $<

src/day%/ans.txt: src/day%/solution.py src/day%/input.txt
	python3 $< > $@


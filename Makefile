.PRECIOUS: src/day%/ans.txt src/day%/input.txt src/day%/solution.py
.PHONY: all %
days := $(shell seq -f "%02g" $$(date -d "$D" '+%d'))

all: $(days)

%: src/day%/ans.txt
	@echo "Day $* --------------------------------------------------"
	@cat $<

src/day%/ans.txt: src/day%/solution.py src/day%/input.txt
	python3 $< > $@

# for .ses see
# www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/
src/day%/input.txt:
	curl https://adventofcode.com/2021/day/$$(echo $* | sed s/^0//)/input \
		--cookie "session=$$(cat .ses)" \
		> $@

src/day%/solution.py:
	touch $@

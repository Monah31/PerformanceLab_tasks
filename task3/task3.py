import json
import sys

if __name__ == "__main__":
    #if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        tests = json.load(f)
    print(tests)

    with open(sys.argv[2]) as f:
        values_t = json.load(f)
    print(values_t)

    # else:
    #
    #     with open('tests.json') as f:
    #         tests = json.load(f)
    #     print(tests)
    #
    #     with open('values.json') as f:
    #         values_t = json.load(f)
    #     print(values_t)


    values = values_t['values']
    print(values)

    report_tests = tests['tests']
    print(report_tests)


    def dictTests(report_tests):
        for test in report_tests:
            for value in values:

                if test["id"] == value["id"]:
                    test["value"] = value["value"]
                elif "values" in test:
                    dictTests(test["values"])
        return report_tests


    tests['tests'] = dictTests(report_tests)
    report_w = json.dumps(tests, indent=2)

    with open(sys.argv[3], "w") as my_file:
        my_file.write(report_w)

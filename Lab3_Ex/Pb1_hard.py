import json

def nr_trecuti(jsonFile):
    with open(jsonFile, 'r') as file:
        data = json.load(file)
    
    passed = 0
    failed = 0
    for student, details in data.items():
        seminarii = sum(details['seminarii']) * 0.2
        proiect = (details['proiect'] ) * 0.2
        partial = (details['partial'] ) * 0.3
        curs = (details['curs'] ) * 0.3
        final = seminarii + proiect + partial + curs
        if final >= 45:
            passed += 1
        else:
            failed += 1
    return passed, failed

def main():
    jsonFile = 'students.json'
    passed, failed = nr_trecuti(jsonFile)
    print(f"Number of students who passed: {passed}")
    print(f"Number of students who failed: {failed}")

if __name__ == "__main__":
    main()
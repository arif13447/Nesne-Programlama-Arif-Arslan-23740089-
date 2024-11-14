#include <iostream>
#include <string>

class Person {
protected:
    std::string name;
    int age;

public:
    Person(std::string name, int age) : name(name), age(age) {}

    virtual std::string display_info() {
        return "Name: " + name + ", Age: " + std::to_string(age);
    }
};

class Student : public Person {
private:
    std::string student_id;

public:
    Student(std::string name, int age, std::string student_id)
        : Person(name, age), student_id(student_id) {}

    std::string display_info() override {
        return "Student - Name: " + name + ", Age: " + std::to_string(age) + ", Student ID: " + student_id;
    }
};

class Teacher : public Person {
private:
    std::string subject;

public:
    Teacher(std::string name, int age, std::string subject)
        : Person(name, age), subject(subject) {}

    std::string display_info() override {
        return "Teacher - Name: " + name + ", Age: " + std::to_string(age) + ", Subject: " + subject;
    }
};

int main() {
    Student student("Ahmet", 20, "235846");
    Teacher teacher("Mr. Ömer", 40, "Matematik");

    std::cout << student.display_info() << std::endl;
    std::cout << teacher.display_info() << std::endl;

    return 0;
}

int main() {
    Student student("Ali", 20, "245682");
    Teacher teacher("Mr. Ömer", 40, "Matematik");

    std::cout << student.display_info() << std::endl;
    std::cout << teacher.display_info() << std::endl;

    return 0;
}

int main() {
    Student student("Ayşe", 20, "235158");
    Teacher teacher("Mr. Ömer", 40, "Matematik");

    std::cout << student.display_info() << std::endl;
    std::cout << teacher.display_info() << std::endl;

    return 0;
}
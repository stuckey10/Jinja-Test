#include <iostream>


class StuckeysTry
{
public:
    StuckeysTry(){}

    
    string getname(){ return m_name;}
    string setname(string name){ m_name = name;}
    
    string getsurname(){ return m_surname;}
    string setsurname(string surname){ m_surname = surname;}
    
    int getage(){ return m_age;}
    int setage(int age){ m_age = age;}
    

private:
    
    string m_name;
    
    string m_surname;
    
    int m_age;
    
}
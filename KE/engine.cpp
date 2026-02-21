#include<iostream>
#include<cmath>
using namespace std;
int main(){
  double ke_city,m,v_city,ke_high,v_high;
  m=1200;
  v_high=22.2;
  v_city=11.1;
  ke_city=0.5*m*(pow(v_city,2));
  ke_high=0.5*m*(pow(v_high,2));
  cout<<"KE in City "<<ke_city<<endl;
  cout<<"KE in Highway "<<ke_high<<endl;

}
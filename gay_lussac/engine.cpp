extern "C"{
  double ctok(double c){
    return c+273.15;
  }
  double p2(double p1,double t1,double t2){
    return (p1*t2)/t1;
  }

}
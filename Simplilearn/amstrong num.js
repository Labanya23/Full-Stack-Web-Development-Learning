
//Program to check an Armstrong number of three digits

//153=1*1*1+5*5*5+3*3*3
//using while loop

var number = 153;
var sum =0 ;

//create a temorary variable

let temp = number;
while(temp>0){
    //finding the one's digit
    var reminder=temp%10;
    sum+= remainder*remainder*remainder;

    //removing last digit from the number

    temp = parseInt(temp/10); //convert float into integer

}
//check the condition

if(sum==number){
    document.write(number+"is an Amstrong number");
}
else{
    document.write(number+"is not an Amstrong number");
}

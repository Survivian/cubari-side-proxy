//The purpose of this script is to aggregate a number of supplied Google Drive URLs and then print it into something usable by Cubari.moe

#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <string>       // String managment funtions.
#include <iostream>     // For input and output
#include <iomanip>      // For i/o manipulators
#include <cmath>        // For math functions.
#include <vector>       // For vector functions.
#include <math.h> 
using namespace std;

//////////////////////////////////////////////////////////////
int urlshort (string &url);

int main() {
    vector<string> urls;
    string myString;
    
    cout << "Please enter some GDrive image URLs:" << endl;

    //This part receives all the inputs.
    do {
        cin >> myString;
        urlshort(myString);
        urls.push_back(myString);
    } while (myString != "0");

    //This gets rid of the final string since it's just a 0.
    urls.pop_back();

    //This part actually outputs the final product.
    cout << '[' << endl;
    for (int i=0; i<urls.size()-1; i++) {
        cout << '"' << urls[i] << '"' << "," << endl;
    }
    cout << '"' << urls.back() << '"' << endl;
    cout << ']' << endl;
    return 0;
}

//This function shaves off the final bit of a GDrive share URL and replaces part of it with the "uc?id" bit.
//This turns the GDrive share link into a direct link. 
int urlshort(string &url) {
    if (url == "0") return 0;
    string ident = "uc?id=";
    char last;
    url.replace(25,7,ident);
    url.erase(url.length() - 17);
    return 0;
}
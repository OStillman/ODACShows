import 'package:flutter/material.dart';

//Colors
Color colour_main = Color.fromRGBO(44,102,110, 1.0);
Color colour_tags = Color.fromRGBO(73,161,173, 1.0);

//Images
Image image_tv = Image.asset('assets/images/tv.png');

RoundedRectangleBorder border_tag = RoundedRectangleBorder(
    borderRadius: BorderRadius.circular(18.0)
);


// Text Styles
TextStyle textstyle_title = TextStyle(
  color: Colors.white,
  fontFamily: 'Raleway',
  fontWeight: FontWeight.bold,
  fontSize: 23,
);

TextStyle textstyle_paragraph = TextStyle(
  color: Colors.white,
  fontFamily: 'Raleway',
  fontWeight: FontWeight.bold,
  fontSize: 15,
);

//Dividers
Divider divider_list = Divider(
  height: 20,
  indent: 60,
  endIndent: 60,
  thickness: 3,
  color: Colors.white,
);
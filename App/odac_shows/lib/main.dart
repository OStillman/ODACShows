import 'package:flutter/material.dart';

import 'helpers/constants.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ODAC Shows',
      theme: ThemeData(
        primaryColor: colour_main,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: TVHomePage(title: 'ODSH - Home'),
      routes: {},
    );
  }
}

class TVHomePage extends StatefulWidget {
  TVHomePage({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _TVHomePageState createState() => _TVHomePageState();
}

class _TVHomePageState extends State<TVHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    final pageController = PageController(
      initialPage: 1,
    );

    return Scaffold(
        appBar: AppBar(
          elevation: 0,
          actions: <Widget>[
            IconButton(
              icon: const Icon(Icons.add),
              onPressed: () {},
            ),
          ],
        ),
        backgroundColor: colour_main,
        body: Center(
            child: PageView(
          controller: pageController,
          scrollDirection: Axis.vertical,
          children: <Widget>[ODView(), main_view(), AllView()],
        )));
  }

  Widget main_view() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          "What's On?",
          style: textstyle_title,
        ),
        Text("19:00", style: textstyle_paragraph),
        divider_list,
        Text(
          "20:00",
          style: textstyle_paragraph,
        ),
        divider_list,
        Text(
          "21:00",
          style: textstyle_paragraph,
        ),
        divider_list,
        Text(
          "22:00",
          style: textstyle_paragraph,
        ),
        divider_list
      ],
    );
  }

  Widget ODView() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          "Find Something...",
          style: textstyle_title,
        ),
        ButtonBar(
          //FYI this works well, unless there are too many buttons, we need to limit one row to 4 ish buttons
          alignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            FlatButton(
              child: Text(
                "Easy",
                style: textstyle_paragraph,
              ),
              color: colour_tags,
              shape: border_tag,
              onPressed: () {},
            ),
            FlatButton(
              child: Text(
                "Comedy",
                style: textstyle_paragraph,
              ),
              color: colour_tags,
              shape: border_tag,
              onPressed: () {},
            ),
            FlatButton(
              child: Text(
                "Drama",
                style: textstyle_paragraph,
              ),
              color: colour_tags,
              shape: border_tag,
              onPressed: () {},
            ),
            FlatButton(
              child: Text(
                "Food",
                style: textstyle_paragraph,
              ),
              color: colour_tags,
              shape: border_tag,
              onPressed: () {},
            ),
          ],
        )
      ],
    );
  }

  Widget AllView() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.start,
      children: <Widget>[
        ButtonBar(
            //FYI this works well, unless there are too many buttons, we need to limit one row to 4 ish buttons
            alignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              FlatButton(
                child: Text(
                  "Live TV",
                  style: textstyle_paragraph,
                ),
                color: colour_tags,
                shape: border_tag,
                onPressed: () {},
              ),
              FlatButton(
                child: Text(
                  "On Demand",
                  style: textstyle_paragraph,
                ),
                color: colour_tags,
                shape: border_tag,
                onPressed: () {},
              ),
            ]),
      ],
    );
  }
}

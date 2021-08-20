import 'package:flutter/material.dart';
import 'on_demand/on_demand_entry.dart';

import 'helpers/constants.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ODAC Shows',
      theme: ThemeData(
        primaryColor: Colors.cyan[900],
        accentColor: Colors.cyan,
        primaryColorDark: Colors.teal[800],
        primaryColorLight: Colors.teal[100],
      ),
      //home: MyHomePage(),
      initialRoute: '/',
      routes: {
        '/': (context) => MyHomePage(),
        '/OD': (context) => OnDemandEntry(),
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text("ODAC Shows"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            Text(
              "Welcome to ODAC Shows!",
              style: TextStyle(fontSize: 40, color: Colors.white),
              textAlign: TextAlign.center,
            ),
            Container(
              child: Column(
                children: <Widget>[
                  TextButton(
                      onPressed: () {
                        Navigator.pushNamed(context, '/OD');
                      },
                      style: ButtonStyle(
                          fixedSize:
                              MaterialStateProperty.all(Size(170.0, 210.0))),
                      child: const Image(
                        image: AssetImage('assets/images/OD.png'),
                      )),
                  Padding(
                    padding: EdgeInsets.only(top: 5),
                    child: TextButton(
                        onPressed: () {
                          Navigator.pushNamed(context, '/OD');
                        },
                        style: ButtonStyle(
                            fixedSize:
                                MaterialStateProperty.all(Size(170.0, 210.0))),
                        child: const Image(
                          image: AssetImage('assets/images/Live.png'),
                        )),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

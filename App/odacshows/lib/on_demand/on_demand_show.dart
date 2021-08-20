import 'package:flutter/material.dart';

import '/helpers/constants.dart';


class OnDemandShow extends StatefulWidget {
  final String show_name;
  final String show_id;

  const OnDemandShow(this.show_name,this.show_id);


  @override
  _OnDemandShow createState() => _OnDemandShow();
}

class _OnDemandShow extends State<OnDemandShow> {
  void _incrementCounter() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[800],
      appBar: AppBar(
        title: Text(widget.show_name),
      ),
      body: Center(
        child: Column(),
      ),
    );
  }
}

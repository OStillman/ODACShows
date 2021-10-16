// To parse this JSON data, do
//
//     final onDemandShows = onDemandShowsFromJson(jsonString);

import 'package:meta/meta.dart';
import 'dart:convert';

class OnDemandShow {
  OnDemandShow({
    required this.odShow,
  });

  List<OdShow> odShow;

  factory OnDemandShow.fromRawJson(String str) => OnDemandShow.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory OnDemandShow.fromJson(Map<String, dynamic> json) => OnDemandShow(
    odShow: List<OdShow>.from(json["od_show"].map((x) => OdShow.fromJson(x))),
  );

  Map<String, dynamic> toJson() => {
    "od_show": List<dynamic>.from(odShow.map((x) => x.toJson())),
  };
}

class OdShow {
  OdShow({
    required this.episode,
    required this.id,
    required this.name,
    required this.series,
    required this.service,
    required this.watching,
  });

  int episode;
  int id;
  String name;
  int series;
  String service;
  String watching;

  factory OdShow.fromRawJson(String str) => OdShow.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory OdShow.fromJson(Map<String, dynamic> json) => OdShow(
    episode: json["episode"],
    id: json["id"],
    name: json["name"],
    series: json["series"],
    service: json["service"],
    watching: json["watching"],
  );

  Map<String, dynamic> toJson() => {
    "episode": episode,
    "id": id,
    "name": name,
    "series": series,
    "service": service,
    "watching": watching,
  };
}

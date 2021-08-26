// To parse this JSON data, do
//
//     final addOnDemandShow = addOnDemandShowFromJson(jsonString);

import 'package:meta/meta.dart';
import 'dart:convert';

class AddOnDemandShow {
  AddOnDemandShow({
    required this.name,
    required this.service,
    required this.watching,
    required this.episode,
    required this.series,
    required this.tags,
  });

  String name;
  int service;
  String watching;
  int episode;
  int series;
  List<String> tags;

  factory AddOnDemandShow.fromRawJson(String str) => AddOnDemandShow.fromJson(json.decode(str));

  String toRawJson() => json.encode(toJson());

  factory AddOnDemandShow.fromJson(Map<String, dynamic> json) => AddOnDemandShow(
    name: json["name"],
    service: json["service"],
    watching: json["watching"],
    episode: json["episode"],
    series: json["series"],
    tags: List<String>.from(json["tags"].map((x) => x)),
  );

  Map<String, dynamic> toJson() => {
    "name": name,
    "service": service,
    "watching": watching,
    "episode": episode,
    "series": series,
    "tags": List<dynamic>.from(tags.map((x) => x)),
  };
}

from pymongo import MongoClient
import csv
import json
import io
import re
import pprint

field map = {
	"name":"name",
	"bodyStyle_label":"bodyStyle",
	"assembly_label":"assembly",
	"class_label":"class",
        "designer_label" : "designer",
    
	"designer_label" : "designer",
        "engine_label" : "engine",
        "length" : "length",
        "height" : "height",
        "width" : "width",
        "weight" : "weight",
        "wheelbase" : "wheelbase",
        "layout_label" : "layout",
        "manufacturer_label" : "manufacturer",
        "modelEndYear" : "modelEndYear",
        "modelStartYear" : "modelStartYear",
        "predecessorLabel" : "predecessorLabel",
        "productionStartYear" : "productionStartYear",    
        "productionEndYear" : "productionEndYear",
        "transmission" : "transmission"

}

fields = field_map.keys()

def skip_lines(input_file,skip):
	for i in range(0,skip):
		next(input_file)

def is_number(s):
    try:
      float(s)		
      return True
    except ValueError:
    	return False

def strip_automobile(v):
      return re.sub(r"\s*\(automobile\)\s*"," ",v)

def strip_city(v):
      return re.sub(r"\s*\(city\)\s*"," ",v)	

def parse_Array(v):
      if(v[0]=="{")and(v[-1]=="}"):
      	v=v.lstrip("{")
      	v=v.rstrip("}")
      	v_array=v.split("|")
      	v_array = [i.strip() for i in v_array]
      	return v_array
      return v
      	


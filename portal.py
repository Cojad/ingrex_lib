#!/usr/bin/env python
# usage: python portal.py LatE6 LngE6
# example : ./portal.py 25167489 121446384
#
from ingrex import Intel, Utils
import json,sys

def getPortalTile(cord):
    xtile, ytile = Utils.calc_tile(cord['LngE6']/1E6, cord['LatE6']/1E6, 15)
    tilekey = '15_{}_{}_8_8_25'.format(xtile, ytile)
    return tilekey

def main():
    "main function"
    cord = {
        'LatE6':float(sys.argv[1]),
        'LngE6':float(sys.argv[2])
    }
    with open('cookies') as cookies:
        cookies = cookies.read().strip()
    intel = Intel(cookies)
    tilekey = getPortalTile(cord)
    result = intel.fetch_map([tilekey])
    entities = result['map'][tilekey]['gameEntities']

    for entity in entities:
        if entity[0].endswith('.16'):
            if entity[2][2] == cord['LatE6'] and entity[2][3] == cord['LngE6'] :
                "print(entity[0],entity[2][2],entity[2][3])"
                guid = entity[0]

    # If anyone want a pretty print json output
    # result = intel.fetch_portal(guid=guid,indent=2,ensure_ascii=False)
    result = intel.fetch_portal(guid=guid)
    print json.dumps(result)

if __name__ == '__main__':
    main()

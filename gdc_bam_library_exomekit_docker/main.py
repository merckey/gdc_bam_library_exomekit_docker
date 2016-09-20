#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys

## how to test ## uncomment "testing" functions, run python with garbage -b -l values with real json input, then:
# $ while read line ; do a=(${line}) && echo python ~/gdc_bam_library_exomekit_docker/gdc_bam_library_exomekit_docker/main.py -j ../bam_libraryname_capturekey.json -b ${a[0]} -l ${a[1]} ; done < bams_libraries.txt | parallel -j 20
# $ while read line ; do echo python ~/gdc_bam_library_exomekit_docker/gdc_bam_library_exomekit_docker/main.py -j ../bam_libraryname_capturekey.json -b ${line} -l asdf ; done < bams.txt | parallel -j 20

#from .decider import get_kits
from decider import get_kits

def setup_logging(args):
    logging.basicConfig(
        filename=os.path.join('output.log'),
        level=args.level,
        filemode='a',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )
    logger = logging.getLogger(__name__)
    return logger

def get_kit_from_capture_kit(capture_kit):
    return

def expl_prop(catalog_number_list, json_data, prop_name):
    prop_dict = dict()
    for catalog_number in catalog_number_list:
        prop_dict[catalog_number] = set()
    for bam_key in sorted(list(json_data.keys())):
        bam_value = json_data.get(bam_key)
        for library_key in sorted(list(json_data.get(bam_key))):
            if library_key == 'analysis_id' or library_key == 'center_name':
                continue
            library_dict = json_data.get(bam_key).get(library_key)
            if 'capture_kits' not in library_dict:
                ### track library free BAMs
                continue
            capture_kits = library_dict.get('capture_kits')
            for capture_kit in capture_kits:
                catalog_number = capture_kit.get('catalog_number')
                prop_value = capture_kit.get(prop_name)
                prop_dict[catalog_number].add(prop_value)
    return prop_dict


def expl_target_prop(target_set_list, json_data, prop_name):
    prop_dict = dict()
    for target_set in target_set_list:
        prop_dict[target_set] = set()
    for bam_key in sorted(list(json_data.keys())):
        bam_value = json_data.get(bam_key)
        for library_key in sorted(list(json_data.get(bam_key))):
            if library_key == 'analysis_id' or library_key == 'center_name':
                continue
            library_dict = json_data.get(bam_key).get(library_key)
            if 'target_set' not in library_dict:
                ### track library free BAMs
                continue
            if 'capture_kits' not in library_dict:
                ### track library free BAMs
                continue
            target_set = library_dict.get('target_set')
            if len(target_set) > 1:
                sys.exit(target_set)
            if len(target_set) == 0:
                continue
            this_target_set = target_set[0]
            capture_kits = library_dict.get('capture_kits')
            for capture_kit in capture_kits:
                #catalog_number = capture_kit.get('catalog_number')
                prop_value = capture_kit.get(prop_name)
                prop_dict[this_target_set].add(prop_value)
    return prop_dict

def get_catalog_number_list(json_data):
    catalog_number_set = set()
    for bam_key in sorted(list(json_data.keys())):
        bam_value = json_data.get(bam_key)
        for library_key in sorted(list(json_data.get(bam_key))):
            if library_key == 'analysis_id' or library_key == 'center_name':
                continue
            library_dict = json_data.get(bam_key).get(library_key)
            if 'capture_kits' not in library_dict:
                ### track library free BAMs
                continue
            capture_kits = library_dict.get('capture_kits')
            for capture_kit in capture_kits:
                catalog_number = capture_kit.get('catalog_number')
                catalog_number_set.add(catalog_number)
    return sorted(list(catalog_number_set))

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def write_dict(data_dict, fname):
    with open(fname, 'w') as f_open:
        json.dump(data_dict, f_open, default=set_default, indent=4, sort_keys=True)
    return

def get_target_set_list(json_data):
    target_set_set = set()
    for bam_key in sorted(list(json_data.keys())):
        bam_value = json_data.get(bam_key)
        for library_key in sorted(list(json_data.get(bam_key))):
            if library_key == 'analysis_id' or library_key == 'center_name':
                continue
            library_dict = json_data.get(bam_key).get(library_key)
            if 'target_set' not in library_dict:
                #print(bam_key)
                continue
            target_sets = library_dict.get('target_set')
            for target_set in target_sets:
                target_set_set.add(target_set)
    return sorted(list(target_set_set))
    

def explore_target_set(json_data):
    target_set_list = get_target_set_list(json_data)
    target_catnum_dict = expl_target_prop(target_set_list, json_data, 'catalog_number')
    target_fileurl_dict = expl_target_prop(target_set_list, json_data, 'cached_target_file_url')
    target_iscustom_dict = expl_target_prop(target_set_list, json_data, 'is_custom')
    target_reagentname_dict = expl_target_prop(target_set_list, json_data, 'reagent_name')
    target_reagentvendor_dict = expl_target_prop(target_set_list, json_data, 'reagent_vendor')
    target_probefile_dict = expl_target_prop(target_set_list, json_data, 'probe_file_url')
    target_targetfile_dict = expl_target_prop(target_set_list, json_data, 'target_file_url')

    write_dict(target_catnum_dict, 'target_catnum.json')
    write_dict(target_fileurl_dict, 'target_fileurl.json')
    write_dict(target_iscustom_dict, 'target_iscustom.json')
    write_dict(target_reagentname_dict, 'target_reagentname.json')
    write_dict(target_reagentvendor_dict, 'target_reagentvendor.json')
    write_dict(target_probefile_dict, 'target_probefile.json')
    write_dict(target_targetfile_dict, 'target_targetfile.json')
    return

def explore_domain(json_data):
    catalog_number_list = get_catalog_number_list(json_data)
    cat_cached_dict = expl_prop(catalog_number_list, json_data, 'cached_target_file_url')
    cat_custom_dict = expl_prop(catalog_number_list, json_data, 'is_custom')
    cat_reagentname_dict = expl_prop(catalog_number_list, json_data, 'reagent_name')
    cat_reagentvendor_dict = expl_prop(catalog_number_list, json_data, 'reagent_vendor')
    cat_probe_dict = expl_prop(catalog_number_list, json_data, 'probe_file_url')
    cat_target_dict = expl_prop(catalog_number_list, json_data, 'target_file_url')

    write_dict(cat_cached_dict, 'cached_target_file_url.json')
    write_dict(cat_custom_dict, 'is_custom.json')
    write_dict(cat_reagentname_dict, 'reagent_name.json')
    write_dict(cat_reagentvendor_dict, 'reagent_vendor.json')
    write_dict(cat_probe_dict, 'probe_file_url.json')
    write_dict(cat_target_dict, 'target_file_url.json')
    return

def write_bams_file(json_data):
    bam_set = set()
    for bam_name in sorted(list(json_data.keys())):
        bam_set.add(bam_name)
    bam_list = sorted(list(bam_set))
    f_name = 'bams.txt'
    with open(f_name, 'w') as f_open:
        for bam_name in bam_list:
            f_open.write(bam_name + '\n')
    return

def write_bams_libraries_file(json_data):
    bam_dict = dict()
    for bam_name in sorted(list(json_data.keys())):
        bam_dict[bam_name] = set()
        bam_data = json_data.get(bam_name)
        bam_keys = sorted(list(bam_data.keys()))
        for bam_key in bam_keys:
            if bam_key == 'target_set' or bam_key == 'center_name' or bam_key == 'analysis_id':
                continue
            library_name = bam_key
            bam_dict[bam_name].add(library_name)
    bam_list = sorted(list(bam_dict))
    f_name = 'bams_libraries.txt'
    with open(f_name, 'w') as f_open:
        for bam_name in bam_list:
            library_list = sorted(list(bam_dict.get(bam_name)))
            for library_name in library_list:
                f_open.write(bam_name + '\t' + library_name + '\n')
    return


def main():
    parser = argparse.ArgumentParser('determine kit(s) used by BAM/library')

    # Logging flags.
    parser.add_argument('-d', '--debug',
        action = 'store_const',
        const = logging.DEBUG,
        dest = 'level',
        help = 'Enable debug logging.',
    )
    parser.set_defaults(level = logging.INFO)

    # Required flags.
    parser.add_argument('-j', '--json_path',
                        required = True
    )
    parser.add_argument('-b', '--bam_name',
                        required = True
    )
    parser.add_argument('-l', '--library_name',
                        required = True
    )

    args = parser.parse_args()
    bam_name = args.bam_name
    json_path = args.json_path
    library_name = args.library_name

    logger = setup_logging(args)

    with open(json_path,'r') as data_file:
        json_data = json.load(data_file)

    ### exploration: may be commented out without affecting purpose ###
    #explore_domain(json_data)
    #explore_target_set(json_data)

    ### testing ###
    #write_bams_file(json_data)
    #write_bams_libraries_file(json_data)

    ### core functionality ###
    kit_list = get_kits(json_data, bam_name, library_name, logger)
    for kit in kit_list:
       f_name = kit + '.kit'
       with open(f_name, 'w') as f_open:
           f_open.write(kit)
    return

if __name__ == '__main__':
    main()

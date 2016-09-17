#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys

from .decider import get_kits

def setup_logging(args):
    logging.basicConfig(
        filename=os.path.join('output.log'),
        level=args.level,
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )
    logger = logging.getLogger(__name__)
    return logger

def get_kit_from_target_set(target_name):
    return

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

def get_kits(json_data, bam_name, library_name, logger):
    library_json = json_data.get(bam_name).get(library_name)
    target_set = library_json.get('target_set')
    if len(target_set) > 1:
        logger.debug('unexpected number of target_set: %s' % target_set)
        sys.exit(1)
    elif len(target_set) == 1:
        target_name = target_set[0]
        kit_name = get_kit_from_target_set(target_name)
        kit_list = [ kit_name ]
        return kit_list
    elif len(target_set) == 0:
        capture_kits = library_json.get('capture_kits')
        for capture_kit in capture_kits:
            kit_list = get_kit_from_capture_kit(capture_kit)
            return kit_list
    logger.debug('should not be here')
    sys.exit(1)
    return

def main():
    parser = argparse.ArgumentParser('determine kit(s) used by BAM library')

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

    ## exploration: may be commented out without affect purpose
    explore_domain(json_data)
    explore_target_set(json_data)

    ## core functionality
    kit_list = get_kits(json_data, bam_name, library_name, logger)
    return

if __name__ == '__main__':
    main()

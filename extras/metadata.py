# -*- coding: utf-8 -*-
__author__ = 'hsercanatli'

import compmusic.dunya.makam as makam
import compmusic
import json

from compmusic import dunya

class MetadataExtractorRecording:
    def __init__(self, mbid):
        print "\n================================================================"
        # connecting to the server
        compmusic.dunya.conn.set_token('b24315d957c8b5bb5fc78abed762764b2d34ca62')
        self.rec_meta = makam.get_recording(mbid)

        # out varieable
        self.out_recording = ""

        # recording variables
        self.mbid = None
        self.title = None

        # release variables
        self.rel_id = None
        self.rel_name = None

        # artist variables
        self.art_id = None
        self.art_name = None

        # work variables
        self.work_id = None
        # self.work_name = None

    def get_mbid(self):

        # getting mbid
        try:
            self.mbid = u''.join(self.rec_meta['mbid']).encode('utf-8').strip()
        except: self.mbid = None

        print "mbid:", self.mbid
        self.out_recording += self.mbid + "\t"

    def get_title(self):

        # getting title
        try: self.title = u''.join(self.rec_meta['title']).encode('utf-8').strip()
        except: self.title += ''
        print "title:", self.title
        self.out_recording += self.title + "\t"

    def get_release(self):
        # release
        try:
            self.rel_id = u''.join(self.rec_meta['releases'][0]['mbid']).encode('utf-8').strip()
            self.rel_name = u''.join(self.rec_meta['releases'][0]['title']).encode('utf-8').strip()
        except:
            self.rel_id = ''
            self.rel_name = ''
        print "release id:", self.rel_id
        print "release name:", self.rel_name
        self.out_recording += self.rel_id + "\t" + self.rel_name + "\t"

    def get_artist(self):
        # artist
        try:
            self.art_id = u''.join(self.rec_meta['artists'][0]['mbid']).encode('utf-8').strip()
            self.art_name = u''.join(self.rec_meta['artists'][0]['name']).encode('utf-8').strip()
        except:
            self.art_id = ''
            self.art_name = ''

        self.out_recording += self.art_id + "\t" + self.art_name + "\t"

        print "artist id:", self.art_id
        print "artist name:", self.art_name

    def get_work(self):
        # work
        try:
            self.work_id = u''.join(self.rec_meta['works'][0]['mbid']).encode('utf-8').strip()
            # self.work_name = u''.join(self.rec_meta['works'][0]['title']).encode('utf-8').strip()
        except:
            self.work_id = ''
            # self.work_name = ''

        self.out_recording += self.work_id # + "\t" + self.work_name

        print "work id:", self.work_id

    def run(self):
        # mbid
        self.get_mbid()
        # title
        self.get_title()
        # release
        self.get_release()
        # artist
        self.get_artist()
        # work
        self.get_work()

        return self.out_recording

class MetadataExtractorWork:
    def __init__(self, workid):
        print "\n================================================================"

        with open("symbTr_mbid.json") as f: self.symbtr_data = json.load(f)

        # connecting to the server
        compmusic.dunya.conn.set_token('b24315d957c8b5bb5fc78abed762764b2d34ca62')
        self.work_meta = makam.get_work(workid)

        # out variable
        self.out_work = ""

        # work variables
        self.work_id = workid
        self.work_title = None

        # symbtr
        self.symbtr = ''

        # composer variables
        self.composer_id = None
        self.composer_name = None

        # makam
        self.makam_id = None
        self.makam_name = None

        # form
        self.form_id = None
        self.form_name = None

        # usul
        self.usul_id = None
        self.usul_name = None

        # recordings
        self.recordings = ''

    def get_workid(self):
        # mbid
        try:
            self.work_id = u''.join(self.work_meta['mbid']).encode('utf-8').strip()
        except: self.work_id = ''

        self.out_work += self.work_id + "\t"
        print "work id:", self.work_id

    def get_symbtr(self):
        # symbtr
        for work in self.symbtr_data:
            if work['uuid']['mbid'] == self.work_id:
                self.symbtr = u''.join(work['name']).encode('utf-8').strip()

        self.out_work += self.symbtr + "\t"
        print "symbtr:", self.symbtr

    def get_title(self):
        # title
        try:
            self.work_title = u''.join(self.work_meta['title']).encode('utf-8').strip()
        except: self.work_title = ''

        self.out_work += self.work_title + "\t"
        print "title:", self.work_title

    def get_composer(self):
        # composer
        try:
            self.composer_id = u''.join(self.work_meta['composers'][0]['mbid']).encode('utf-8').strip()
            self.composer_name = u''.join(self.work_meta['composers'][0]['name']).encode('utf-8').strip()
        except:
            self.composer_id = ''
            self.composer_name = ''

        self.out_work += self.composer_id + "\t" + self.composer_name + "\t"

        print "composer id:", self.composer_id
        print "composer name:", self.composer_name

    def get_makam(self):
        # makam
        try:
            self.makam_id = u''.join(self.work_meta['makams'][0]['uuid']).encode('utf-8').strip()
            self.makam_name = u''.join(self.work_meta['makams'][0]['name']).encode('utf-8').strip()

        except:
            self.makam_id = ''
            self.makam_name = ''

        self.out_work += self.makam_id + "\t" + self.makam_name + "\t"

        print "makam id:", self.makam_id
        print "makam name:", self.makam_name

    def get_form(self):
        # form
        try:
            self.form_id = u''.join(self.work_meta['forms'][0]['uuid']).encode('utf-8').strip()
            self.form_name = u''.join(self.work_meta['forms'][0]['name']).encode('utf-8').strip()

        except:
            self.form_id = ''
            self.form_name = ''

        self.out_work += self.form_id + "\t" + self.form_name + "\t"

        print "form id:", self.form_id
        print "form name:", self.form_name

    def get_usul(self):
        # usul
        try:
            self.usul_id = u''.join(self.work_meta['usuls'][0]['uuid']).encode('utf-8').strip()
            self.usul_name = u''.join(self.work_meta['usuls'][0]['name']).encode('utf-8').strip()

        except:
            self.usul_id = ''
            self.usul_name = ''

        self.out_work += self.usul_id + "\t" + self.usul_name + "\t"

        print "usul id:", self.usul_id
        print "usul name:", self.usul_name

    def get_recordings(self):
        # recordings
        try:
            for recording in self.work_meta['recordings']: self.recordings += recording['mbid'] + ", "
            self.out_work += u''.join(self.recordings[:-2]).encode('utf-8').strip()

        except:
            self.recordings = ''
            self.out_work += self.recordings

        print "recordings:", self.recordings[:-2]

    def run(self):
        # work id
        self.get_workid()

        # symbtr
        self.get_symbtr()

        # title
        self.get_title()

        # composer
        self.get_composer()

        # makam
        self.get_makam()

        # form
        self.get_form()

        # usul
        self.get_usul()

        # recordings
        self.get_recordings()

        return self.out_work

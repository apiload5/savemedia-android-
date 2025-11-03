import json
from kivy.utils import platform
from kivy.logger import Logger

class AdManager:
    def __init__(self):
        self.initialized = False
        self.setup_ads()
    
    def setup_ads(self):
        """Initialize ad networks"""
        try:
            if platform == 'android':
                self.setup_android_ads()
            else:
                # For desktop testing
                self.setup_mock_ads()
            
            self.initialized = True
            Logger.info('AdManager: Ads initialized successfully')
            
        except Exception as e:
            Logger.error(f'AdManager: Setup failed - {e}')
    
    def setup_android_ads(self):
        """Initialize AdMob for Android"""
        try:
            from jnius import autoclass
            
            # Load AdMob classes
            MobileAds = autoclass('com.google.android.gms.ads.MobileAds')
            AdRequest = autoclass('com.google.android.gms.ads.AdRequest')
            AdView = autoclass('com.google.android.gms.ads.AdView')
            InterstitialAd = autoclass('com.google.android.gms.ads.InterstitialAd')
            
            # Initialize AdMob SDK
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.activity = PythonActivity.mActivity
            
            MobileAds.initialize(self.activity)
            
            # Create ad request builder
            self.ad_request_builder = AdRequest.Builder()
            
            # Setup interstitial ad
            self.setup_interstitial_ad()
            
            Logger.info('AdManager: Android ads setup complete')
            
        except Exception as e:
            Logger.error(f'AdManager: Android setup failed - {e}')
    
    def setup_interstitial_ad(self):
        """Setup interstitial ad for downloads"""
        try:
            from jnius import autoclass
            
            InterstitialAd = autoclass('com.google.android.gms.ads.InterstitialAd')
            
            # Load config
            with open('config.json') as f:
                config = json.load(f)
            
            self.interstitial_ad = InterstitialAd(self.activity)
            self.interstitial_ad.setAdUnitId(config['ads']['admob']['interstitial_ad_id'])
            
            # Load the ad
            ad_request = self.ad_request_builder.build()
            self.interstitial_ad.loadAd(ad_request)
            
            Logger.info('AdManager: Interstitial ad loaded')
            
        except Exception as e:
            Logger.error(f'AdManager: Interstitial setup failed - {e}')
    
    def show_interstitial_ad(self):
        """Show interstitial ad"""
        try:
            if (hasattr(self, 'interstitial_ad') and 
                self.interstitial_ad.isLoaded()):
                self.interstitial_ad.show()
                Logger.info('AdManager: Interstitial ad shown')
                return True
            else:
                Logger.warning('AdManager: Interstitial ad not loaded')
                return False
        except Exception as e:
            Logger.error(f'AdManager: Show interstitial failed - {e}')
            return False
    
    def setup_mock_ads(self):
        """Mock ads for desktop testing"""
        Logger.info('AdManager: Mock ads setup for desktop')
    
    def show_mock_ad(self):
        """Show mock ad for testing"""
        Logger.info('AdManager: Mock ad shown')
        return True

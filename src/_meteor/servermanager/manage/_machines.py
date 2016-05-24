from __future__ import absolute_import
from __future__ import print_function
from ...common._base import BaseServer
########################################################################
class Machines(BaseServer):
    """
       This resource represents a collection of all the server machines that
       have been registered with the site. It other words, it represents
       the total computing power of your site. A site will continue to run
       as long as there is one server machine online.
       For a server machine to start hosting GIS services, it must be
       grouped (or clustered). When you create a new site, a cluster called
       'default' is created for you.
       The list of server machines in your site can be dynamic. You can
       register additional server machines when you need to increase the
       computing power of your site or unregister them if you no longer
       need them.
    """
    _machines = None
    _json_dict = None
    _con = None
    _url = None
    _json = None
    _DatastoreMachines = None
    _Protocal = None
    #----------------------------------------------------------------------
    def __init__(self, url, connection,
                 initialize=False):
        """Constructor
            Inputs:
               url - admin url
               connection - SiteConnection object
               initialize - loads the machine information
        """
        super(Machines, self).__init__(url=url,
                                       connection=connection,
                                       initialize=initialize)
        self._url = url
        self._con = connection
        if initialize:
            self.init(connection)
    #----------------------------------------------------------------------
    @property
    def DatastoreMachines(self):
        """returns the datastore machine list"""
        if self._DatastoreMachines is None:
            self.init()
        return self._DatastoreMachines
    #----------------------------------------------------------------------
    @property
    def Protocol(self):
        """returns the protocal"""
        if self._Protocal is None:
            self.init()
        return self._Protocal
    #----------------------------------------------------------------------
    @property
    def machines(self):
        """  returns the list of machines in the cluster """
        machines = []
        if self._machines is None:
            self.init()
        if isinstance(self._machines, list):
            for m in self._machines:
                machines.append(
                    Machine(url=self._url +"/%s" % m['machineName'],
                            connection=self._con))
        return machines
    #----------------------------------------------------------------------
    def getMachine(self, machineName):
        """returns a machine object for a given machine
           Input:
              machineName - name of the box ex: SERVER.DOMAIN.COM
        """
        url = self._url + "/%s" % machineName
        return Machine(url=url,
                       connection=self._con)
    #----------------------------------------------------------------------
    def registerMachine(self, machineName, adminURL):
        """
           For a server machine to participate in a site, it needs to be
           registered with the site. The server machine must have ArcGIS
           Server software installed and authorized.
           Registering machines this way is a "pull" approach to growing
           the site and is a convenient way when a large number of machines
           need to be added to a site. In contrast, a server machine can
           choose to join a site.
           Inputs:
              machineName - name of the server machine
              adminURL - URL wher ethe Administrator API is running on the
                         server machine.
                         Example: http://<machineName>:6080/arcgis/admin
           Output:
              JSON message as dictionary
        """
        params = {
            "f" : "json",
            "machineName" : machineName,
            "adminURL" : adminURL
        }
        url = "%s/register" % self._url
        return self._con.post(path_or_url=url, postdata=params)
    #----------------------------------------------------------------------
    def renameMachine(self, machineName, newMachineName):
        """
           You must use this operation if one of the registered machines
           has undergone a name change. This operation updates any
           references to the former machine configuration.
           By default, when the server is restarted, it is capable of
           identifying a name change and repairing itself and all its
           references. This operation is a manual call to handle the
           machine name change.
           Input:
              machineName - The former name of the server machine that is
                            registered with the site.
              newMachineName - The new name of the server machine.
           Output:
              JSON messages as dictionary
        """
        params = {
            "f" : "json",
            "machineName" : machineName,
            "newMachineName" : newMachineName
        }
        url = self._url + "/rename"
        return self._con.post(path_or_url=url, postdata=params)
########################################################################
class Machine(BaseServer):
    """
       A server machine represents a machine on which ArcGIS Server
       software has been installed and licensed. A site is made up one or
       more of such machines that work together to host GIS services and
       data and provide administrative capabilities for the site. Each
       server machine is capable of performing all these tasks and hence a
       site can be thought of as a distributed peer-to-peer network of such
       machines.
       A server machine communicates with its peers over a range of TCP and
       UDP ports that can be configured using the edit operation. For a
       server machine to host GIS services, it needs to be added to a
       cluster. Starting and stopping the server machine enables and
       disables, respectively, its ability to host GIS services.
       The administrative capabilities of the server machine are available
       through the ArcGIS Server Administrator API that can be accessed
       over HTTP(S). For a server machine to participate in a site, it must
       be registered with the site. A machine can participate in only one
       site at a time. To remove a machine permanently from the site, you
       can use the unregister operation.
    """
    _appServerMaxHeapSize = None
    _webServerSSLEnabled = None
    _webServerMaxHeapSize = None
    _platform = None
    _adminURL = None
    _machineName = None
    _ServerStartTime = None
    _webServerCertificateAlias = None
    _socMaxHeapSize = None
    _synchronize = None
    _configuredState = None
    _ports = None
    _json = None
    _json_dict = None
    _con = None
    _url = None
    #----------------------------------------------------------------------
    def __init__(self, url, connection,
                 initialize=False):
        """Constructor
            Inputs:
               url - admin url
               connection - SiteConnection object
               initialize - boolean - loads properties at creation of object
        """
        super(Machine, self).__init__(url=url,
                                      connection=connection,
                                      initialize=initialize)
        self._url = url
        self._con = connection
        self._currentURL = url
        if initialize:
            self.init(connection)
    #----------------------------------------------------------------------
    @property
    def appServerMaxHeapSize(self):
        """ returns the app server max heap size """
        if self._appServerMaxHeapSize is None:
            self.init()
        return self._appServerMaxHeapSize
    #----------------------------------------------------------------------
    @property
    def webServerSSLEnabled(self):
        """ SSL enabled """
        if self._webServerSSLEnabled is None:
            self.init()
        return self._webServerSSLEnabled
    #----------------------------------------------------------------------
    @property
    def webServerMaxHeapSize(self):
        """ returns the web server max heap size """
        if self._webServerMaxHeapSize is None:
            self.init()
        return self._webServerMaxHeapSize
    #----------------------------------------------------------------------
    @property
    def platform(self):
        """ returns the platform information """
        if self._platform is None:
            self.init()
        return self._platform
    #----------------------------------------------------------------------
    @property
    def adminURL(self):
        """ returns the administration URL """
        if self._adminURL is None:
            self.init()
        return self._adminURL
    #----------------------------------------------------------------------
    @property
    def machineName(self):
        """ returns the machine name """
        if self._machineName is None:
            self.init()
        return self._machineName
    #----------------------------------------------------------------------
    @property
    def ServerStartTime(self):
        """ returns the server start date/time """
        if self._ServerStartTime is None:
            self.init()
        return self._ServerStartTime
    #----------------------------------------------------------------------
    @property
    def webServerCertificateAlias(self):
        """ returns the webserver cert alias"""
        if self._webServerCertificateAlias is None:
            self.init()
        return self._webServerCertificateAlias
    #----------------------------------------------------------------------
    @property
    def socMaxHeapSize(self):
        """ returns the soc's max heap size """
        if self._socMaxHeapSize is None:
            self.init()
        return self._socMaxHeapSize
    #----------------------------------------------------------------------
    @property
    def synchronize(self):
        """synchronize value"""
        if self._synchronize is None:
            self.init()
        return self._synchronize
    #----------------------------------------------------------------------
    @property
    def ports(self):
        """ returns the used ports """
        if self._ports is None:
            self.init()
        return self._ports
    #----------------------------------------------------------------------
    @property
    def configuredState(self):
        """ returns the configured state """
        if self._configuredState is None:
            self.init()
        return self._configuredState
    #----------------------------------------------------------------------
    @property
    def status(self):
        """ returns the state """
        uURL = self._url + "/status"
        params = {
            "f" : "json",
        }
        return self._con.get(path_or_url=uURL, params=params)
    #----------------------------------------------------------------------
    def startMachine(self):
        """ Starts the server machine """
        params = {
            "f" : "json"
        }
        uURL = self._url + "/start"
        return self._con.post(path_or_url=uURL, postdata=params)
    #----------------------------------------------------------------------
    def stopMachine(self):
        """ Stops the server machine """
        params = {
            "f" : "json"
        }
        uURL = self._url + "/stop"
        return self._con.post(path_or_url=uURL, postdata=params)
    #----------------------------------------------------------------------
    def unregisterMachine(self):
        """
           This operation causes the server machine to be deleted from the
           Site.
           The server machine will no longer participate in the site or run
           any of the GIS services. All resources that were acquired by the
           server machine (memory, files, and so forth) will be released.
           Typically, you should only invoke this operation if the machine
           is going to be shut down for extended periods of time or if it
           is being upgraded.
           Once a machine has been unregistered, you can create a new site
           or join an existing site.
        """
        params = {
            "f" : "json"
        }
        uURL = self._url + "/start"
        return self._con.post(path_or_url=uURL, postdata=params)

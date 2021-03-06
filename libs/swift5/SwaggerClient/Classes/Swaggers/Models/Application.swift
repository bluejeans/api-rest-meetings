//
// Application.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Application: Codable {

    /** A summary of the client application. */
    public var _description: String?
    /** The name of the client application. */
    public var appName: String?
    /** A URL of an image that will be displayed to users during authorization. */
    public var appLogoUrl: String?
    public var redirectUrls: [String]?
    /** The client ID will be generated on creation of the application. Normally, a 32 character hexadecimal numeric string. */
    public var clientId: String?
    /** The client secret will be generated on creation of the application. Retain this value as it will only be revealed one time. If lost, you will need to regenerate. */
    public var clientSecret: String?

    public init(_description: String?, appName: String?, appLogoUrl: String?, redirectUrls: [String]?, clientId: String?, clientSecret: String?) {
        self._description = _description
        self.appName = appName
        self.appLogoUrl = appLogoUrl
        self.redirectUrls = redirectUrls
        self.clientId = clientId
        self.clientSecret = clientSecret
    }

    public enum CodingKeys: String, CodingKey { 
        case _description = "description"
        case appName
        case appLogoUrl
        case redirectUrls
        case clientId
        case clientSecret
    }


}


//
// GrantClientScope.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct GrantClientScope: Codable {

    /** The ID of your enterprise. */
    public var enterprise: Int?
    /** The name of the partition you are on. */
    public var partitionName: String?
    public var partition: Partition?

    public init(enterprise: Int?, partitionName: String?, partition: Partition?) {
        self.enterprise = enterprise
        self.partitionName = partitionName
        self.partition = partition
    }


}

